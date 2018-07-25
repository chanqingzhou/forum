from django.core.management.base import BaseCommand, CommandError
from pyp.models import *
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file1 = open("faculty.txt", "r")
        for f in file1:
            f=f.strip()
            if Faculty.objects.filter(faculty_text=f):
                continue
            else:
                test = Faculty(faculty_text=f)
                test.save()
                self.stdout.write(self.style.SUCCESS('added ' + f))
        lis=[['Electrical Engineering', 'EE'],
            ['Civil and Environment Engineering', 'CE'],
            ['Mechanical Engineering', 'ME'],
            ['Biomedical Engineering', 'BN'],
            ['Chemical Engineering', 'CN'],
            ['Materials Science Engineering', 'MLE'],
            ['Mathematics and Applied Mathematics', 'MA'],
            ['Statistics and Applied Statistics', 'ST'],
            ['Chemistry', 'CM'],
            ['Physics', 'PC'],
            ['Life Sciences', 'LSM', 'LSE'],
            ['Pharmacy', 'PR'],
            ['Computational Biology', 'BL'],
            ['Psychology', 'PL'],
            ['Geography', 'GE'],
            ['History', 'HY'],
            ['Japanese Studies', 'JS'],
            ['Chinese Studies', 'CH'],
            ['Sociology', 'SC'],
            ['Philosophy', 'PH'],
            ['Global Studies', 'GL'],
            ['Social Work', 'SW'],
            ['Political Science', 'PS'],
            ['Communicatons and New Media', 'NM'],
            ['School of Business', 'AC'],
            ['School Of Computing', 'CS', 'IS', 'BA'],
            ['School of Law', 'LC', 'LL']
             ]
        file2=open("module.txt","r")
        for f in file2:
            f=f.strip()
            done=False
            if Module.objects.filter(module_code=f):
                continue;
            for codes in lis:
                if f[0:2] in codes:
                    faculty=get_object_or_404(Faculty,faculty_text=codes[0])
                    faculty.module_set.create(module_text="just testing",module_code=f)
                    done =True
                    break;
            if done:
                self.stdout.write(self.style.SUCCESS('added '+ f))

            self.stdout.write(self.style.SUCCESS('Successfully closed poll'))