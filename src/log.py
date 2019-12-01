from datetime import datetime

def log(cols,log_info):
    now = datetime.now()
    dt_string = now.strftime("%m-%d-%Y_%H:%M:%S")

    file = open('logs/{}.txt'.format(dt_string),'w')


    file.write('Modeling Tests ran at {}'.format(dt_string))
    file.write('\n')
    file.write('\n')
    file.write('---------Features Included-----------')
    file.write('\n')
    for each in cols:
        file.write(each)
        file.write('\n')
    file.write('\n')
    file.write('\n')
    for each in log_info:
        file.write('---------{}-----------'.format(each))
        file.write('\n')
        file.write(log_info[each][0])
        file.write('\n')
        file.write('\n')
        file.write('{} Accuracy : {} \n'.format(each,round(log_info[each][1],2)))
        file.write('\n')
        for feat in log_info[each][2]:
            file.write(str(feat))
            file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
        file.write('\n')
    file.close()
    return "Logged Successfully"


