#########################
# Emy's GetVersionInfo.py
#########################
# This script will provide version for installed packages   
# use pkg_Resources module  
import pkg_resources  
from pkg_resources import get_distribution
packages=["numpy", "scipy", "scikit-learn", "statsmodels", "cv2", "sqlite3", "bs4", "nltk",]

##should be like for pk in packages.next()

def print_version(pk):
    try:
        print("*"*25)
        print(f"{pk} : {get_distribution(pk)}")
    except Exception as e:
        try:
            exec(f"import {pk}")
            exec(f"print(pk + ' : '+ {pk}.__version__)")
        except Exception as e1:
            try:
                exec(f"print(pk + ' : '+ {pk}.version)")
            except Exception as e2:
                print(f"{pk} exception trying to import: {e2}, {type(e2)}\n")
                raise e2
                
# def ver_dictr(packages):
#     "version dictionary getter"
#     ver_dict = dict() # "version dictionary"
#     for pk in packages:
#         try:
#             #print("*"*25)
#             print(f"{pk} : {get_distribution(pk)}")
#             ver_dict[pk] = get_distribution(pk)
#         except Exception as e:
#             try:
#                 exec(f"import {pk}")
#                 exec(f"print(pk + ' : '+ {pk}.__version__)")
                
#                 x0 = ver_dict[pk] = exec(f"{pk}.__version__")
#                 print(f"x0 : {x0}")
#             except Exception as e1:
#                 try:
#                     ver_dict[pk] = exec(f"{pk}.version")
#                 except Exception as e2:
#                     print(f"{pk} exception trying to import: {e2}, {type(e2)}\n")
#                     raise e2
#     return( ver_dict )


if __name__ == "__main__":
    #ver_dict = ver_dictr(packages)
    for pk in packages:
        print_version(pk)