import os

file_dict = {}
for root, dirs,files in os.walk("./files_for_task_3"):  
    for filename in files:
        file_body = []
        count_str = 0
        path = os.path.join(root,filename)
        with open(path,'r',encoding= 'utf=8') as f:
            for line in f:
                file_body += [line]
                count_str += 1
            file_dict[filename] = [count_str, file_body]

order_list = [[val[0],key] for key,val in file_dict.items()]
catalog = os.getcwd()
with open(os.path.join(catalog, 'itog.txt'), 'w', encoding='utf-8') as file:
    for i in sorted(order_list):       
        file.write(f'{i[1]}\n')
        file.write(f'{str(i[0])}\n')
        s = file_dict[i[1]][1]
        file.writelines(s)
        

