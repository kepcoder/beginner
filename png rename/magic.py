
            #IT RENAME ALL PNG FILES BY a,b,c,d,... THAT EXISTS ON YOUR PC 


# import os 
# files = os.listdir("png")
# # i = 1
# i = ["a","b","c","d","e","f","g","h","i","j","k","l"]
# for file,new_name in zip(files, i):
#     if file.endswith(".png"):
#         os.rename(f"png/{file}" , f"png/{new_name}.png")
#         # i = i+1
#         print(file)

  
      #IT RENAME ALL PNG FILES BY 1,2,3,4,,5... THAT EXISTS ON YOUR PC

import os 
files = os.listdir("png")
i = 1
# i = ["a","b","c","d","e","f","g","h","i","j","k","l"]
for file in files:
    if file.endswith(".png"):
        os.rename(f"png/{file}" , f"png/{i}.png")
        i = i+1
        print(file)
