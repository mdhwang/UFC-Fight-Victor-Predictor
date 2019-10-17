from datetime import datetime

def log(cols,RF_FeatImp,RF_Acc,RF_Params):
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
    file.write('---------RANDOM FOREST-----------')
    file.write('\n')
    file.write(RF_Params)
    file.write('\n')
    file.write('\n')
    file.write('RF Accuracy : {} \n'.format(round(RF_Acc,2)))
    file.write('\n')
    for each in RF_FeatImp:
        file.write(str(each))
        file.write("\n")
    file.close()
    return "Logged Successfully"


