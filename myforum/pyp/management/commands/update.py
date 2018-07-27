from django.core.management.base import BaseCommand, CommandError
from pyp.models import *
from django.shortcuts import get_object_or_404

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        file1 = open("faculty.txt", "r")
        for f in file1:
            f=f.strip()
            f=f.split(" ", 1)
            if Faculty.objects.filter(faculty_code=f[0].strip()):
                continue
            else:
                test = Faculty(faculty_text=f[1].strip(),faculty_code=f[0].strip())
                test.save()
                self.stdout.write(self.style.SUCCESS('added ' + f[1]))

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
            ['Economics','EC'],
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
            ['School of Business', 'ACC','DSC'],
            ['School Of Computing', 'CS', 'IS', 'BA', 'BT'],
            ['School of Law', 'LC', 'LL']
             ]
        file2=open("module.txt","r")
        for f in file2:
            f=f.strip()
            f=f.split(" ",1)
            fcode=f[0]
            counter=0
            if fcode[2].isdigit():
                fcode = fcode[0:2]
            else:
                fcode = fcode [0:3]
            done=False
            if Module.objects.filter(module_code=f[0].strip()):
                self.stdout.write("already add "+f[0])

                continue;
            for codes in lis:
                for code in  codes[1:]:
                    if fcode==code:
                        print(codes[0])

                        faculty=get_object_or_404(Faculty,faculty_text=codes[0].strip())
                        module=faculty.module_set.create(module_text=f[1],module_code=f[0])
                        done =True
                        x = 2018
                        for count in range(0, 3):
                            module.moduleyear_set.create(year=str(x - count) + "Sem2")
                            module.moduleyear_set.create(year=str(x - count) + "Sem1")
                        break;
                if done:
                    break;
            if done:
                self.stdout.write(self.style.SUCCESS('added '+ f[0]+ " "+f[1]))
            else:
                self.stdout.write("unable to add "+f[0])
