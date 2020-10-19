def main(text,copy=False,font='C:\Windows\Fonts\msyh.ttc',size=(32,32)):
    import pyperclip
    import numpy as np
    from PIL import Image
    import pygame
    if len(text)!=1:
        raise NameError('Can only 1 word!')
    pygame.init()
    font = pygame.font.Font(font, 64)    #Chiness words
    ftext = font.render(text, True, (0,0,0),(255, 255, 255))
    filename = text+'.jpg'
    pygame.image.save(ftext, filename)
    image = Image.open(filename)
    image = image.convert("RGB")
    image = image.resize((19,19))
    print(image.size)
    #image.show()
    img = np.array(image).tolist()
    out = ''
    a = 0
    for x in img:
        for y in x:
            for z in y:
                if y[0]+y[1]+y[2]>562:
                    out = out+' '
                else:
                    out = out+text
                # if y[0]+y[1]+y[2]<382.5:
                #     out = out+text
                # else:
                #     out = out+' '
        out = out+'\n'
    print((out))
    if copy==True:
        pyperclip.copy(out)
    return out


if __name__ == '__main__':
    main('中',copy=True)


