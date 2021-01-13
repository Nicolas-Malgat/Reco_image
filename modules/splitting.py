import os, shutil
import subprocess
from random import sample

class Splitting():

    @staticmethod
    def list_dossiers(dossier):
        dossiers = os.listdir(dossier)
        print(dossiers)

    @staticmethod
    def copie_dossiers(dossier_racine, dossiers_a_garder, nb_images, explorer = False):
        """ Copie les fichiers donnes dans le dossier_cible

        Args:
            dossier_racine (str): chemin du dossier contenant les dossiers des images
            dossiers_a_garder (list<str>): dossiers d'images a garder
            dossier_cible (str): chemin dans lequel on copie les dossiers a garder
            explorer (boolean): defini si dossier_cible s'ouvre dans l'explorateur

        Raises:
            Exception: un des dossier de dossiers_a_garder n'existe pas
        """
        
        path_list = dossier_racine.split('/')
        dossier_cible = os.sep.join(path_list[:-1]) + os.sep + path_list[-1] + "_" + "_".join(dossiers_a_garder)
        dossier_cible = os.path.abspath(dossier_cible)

        if Splitting.__create_path(dossier_cible):

            try:
                for dossier in dossiers_a_garder:
                    print('Creation du dossier ' + dossier)
                    
                    if dossier in os.listdir(dossier_racine):
                        sous_dossier_racine = dossier_racine + os.sep + dossier
                        sous_dossier_cible = dossier_cible + os.sep + dossier
                        os.mkdir(sous_dossier_cible)
                        Splitting.__copy_folder(sous_dossier_racine, sous_dossier_cible, nb_images)
                    else:
                        raise Exception('Dossier non trouve' + str(dossier))
            except Exception as e:
                os.removedirs(dossier_cible)
                raise Exception(e)
            
            if explorer:
                subprocess.Popen(f'explorer /select,"{dossier_cible}"')
        return dossier_cible

    @staticmethod
    def __create_path(dossier):
        if os.path.exists(dossier) == False:
            try:
                os.makedirs(dossier)
            except OSError:
                print (f"Creation of the directory {dossier} failed")
                exit(1)
            else:
                print (f"Successfully created the directory {dossier}")
                return True
        else:
            print(f'Le dossier {dossier} existe déjà !')
            return False

    @staticmethod
    def __copy_folder(dossier, dossier_cible, nb_images):

        images = os.listdir(dossier)
        images = sample(images, nb_images)

        for image in images:
            image_origine = os.path.join(dossier, image)
            image_cible = os.path.join(dossier_cible, image)

            if os.path.isfile(image_origine):
                shutil.copy(image_origine, image_cible)

if __name__ == "__main__":

    # print(os.getcwd())

    dossier_racine = '../datas/RAW/train'
    dossiers_a_garder = ['bus', 'tank']
    dossier_cible = '../datas/RAW/' + dossier_racine.split('/')[-1] + '_' + "_".join(dossiers_a_garder)

    Splitting.copie_dossiers(
        '../datas/RAW/train',
        ['bus', 'tank'],
        250,
        True
    )
    # Splitting.list_dossiers(dossier_racine)