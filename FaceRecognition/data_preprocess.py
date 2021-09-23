from preprocess import preprocesses

input_datadir = './train_img'
output_datadir = './detected_img'

def img_preprocess():
    obj=preprocesses(input_datadir,output_datadir)
    nrof_images_total,nrof_successfully_aligned=obj.collect_data()

    print('Total number of images: %d' % nrof_images_total)
    print('Number of successfully detected images: %d' % nrof_successfully_aligned)



