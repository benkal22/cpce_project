from typing import Any
from django.core.management.base import BaseCommand
from django.utils import timezone

import pandas as pd
from sqlalchemy import create_engine
import os

#Importation des données excel de la nomenclature des secteurs d'activités 

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args: Any, **options: Any) -> str | None:
        #Lecture données excel de nomenclature des secteurs d'activités
        # data = pd.read_excel('nomenclature.xlsx')
        
        # # Obtenir le chemin absolu du répertoire contenant votre script Python
        # script_dir = os.path.dirname(os.path.abspath(__file__))

        # # Spécifier le chemin relatif vers la db
        # db_file_path = os.path.join(script_dir, 'nomenclature_secteurs_activites.xlsx')
       
        # #Connexion à la bd existente
        # # db_engine = create_engine('sqlite:///db.sqlite3')
        # db_engine = create_engine('sqlite:///'.db_file_path)
        
        # #Ecriture des données dans une nouvelle table dans la base de données existante
        # data.to_sql('db', db_engine, index=False, if_exists='append')

        repertoire_script = os.path.dirname(os.path.abspath(__file__))
        file_name = "nomenclature.csv"
        path_file = os.path.join(repertoire_script, file_name)
        data = pd.read_csv(path_file, encoding="ISO-8859-1", delimiter=";")

        
        #Connexion à la bd existente
        db_engine = create_engine('sqlite:///db.sqlite3')
        # db_engine = create_engine('sqlite:///'.db_file_path)
        
        #Ecriture des données dans une nouvelle table dans la base de données existante
        data.to_sql('db', db_engine, index=False, if_exists='append')
        
        # self.stdout.write(path_file)
        self.stdout.write(self.style.SUCCESS('Données importées avec succès depuis Excel vers la base de données'))



