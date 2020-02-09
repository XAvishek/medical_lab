from django.core.management.base import BaseCommand
from medical_lab.views import Patient, Doctor, TestCategory

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str, help='The txt file that contains the name')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                
