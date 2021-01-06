import os, shutil
import subprocess

class Splitting():

    @staticmethod
    def split(dossier_racine, dossiers_a_garder, target, explorer = False):
        """ Copie les fichiers donnes dans le chemin target

        Args:
            dossier_racine (str): chemin du dossier contenant les dossiers des images
            dossiers_a_garder (list<str>): dossiers d'images a garder
            target (str): chemin dans lequel on copie les dossiers a garder
            explorer (boolean): defini si target est ouvert dans l'explorateur

        Raises:
            Exception: un des dossier de dossiers_a_garder n'existe pas
        """

        Splitting.__test_path(target)

        for dossier in dossiers_a_garder:
            
            if dossier in os.listdir(dossier_racine):
                Splitting.__copy_folder(dossier_racine + os.sep + dossier, target)
            else:
                raise Exception('Dossier non trouve' + str(dossier))
        
        if explorer:
            target = os.path.abspath(target)
            subprocess.Popen(f'explorer /select,"{target}"')

    @staticmethod
    def __test_path(target):
        if os.path.exists(target) == False:
            try:
                os.makedirs(target)
            except OSError:
                print (f"Creation of the directory {target} failed")
                exit(1)
            else:
                print (f"Successfully created the directory {target}")

    @staticmethod
    def __copy_folder(src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isfile(s):
                shutil.copy(s, d)

if __name__ == "__main__":

    # print(os.getcwd())

    dossier_racine = '../datas/RAW/train'
    dossiers_a_garder = ['apple', 'bee']
    target = '../datas/RAW/train_' + "_".join(dossiers_a_garder)

    Splitting.split(dossier_racine, dossiers_a_garder, target)