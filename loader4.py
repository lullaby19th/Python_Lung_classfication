import   csv
import  os
import  re
import  cv2
import  random
import  numpy  as  np

def  image_load(path):
    file_list = os.listdir(path)
    file_name = []
    for  i  in  file_list:
        a = int(  re.sub('[^0-9]', '', i )  ) # 숫자가 아닌것은 '' 로 처리 
        file_name.append(a) 
    file_name.sort()

    file_res = [] 
    for  j  in   file_name:
        file_res.append('%s\\%d.png' %(path,j)  )

    image = []
    for  k  in  file_res:
        img = cv2.imread(k)
        image.append(img)

    return  np.array(image)

def  label_load( path ):
    file = open(path)
    labeldata = csv.reader(file)
    labellist = []
    for  i   in  labeldata:
        labellist.append(i)

    label = np.array(labellist)
    label = label.astype(int)  # 숫자로 변환 
    label = np.eye(2)[label]
    label = label.reshape(-1,2) 
    return  label


def  shuffle_batch( data_list, label ):
    x = np.arange( len( data_list) )
    random.shuffle(x)
    data_list2 = data_list[x]
    label2 = label[x]
    return   data_list2, label2 


def  next_batch( data1, data2, init,  fina ):
    return  data1[ init : fina ],  data2[init : fina] 