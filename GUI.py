import PySimpleGUI as sg
import FastFourierTransforms as FFT # my custom implementation of Fast Fourier Transform

def main():
    sg.theme('BrightColors')
    equation_font = ('Helvetica', 11, 'bold')
    layout = [  [sg.Text("Welcome to Fast Fourier Transform SimpleMade! :)")],
                [sg.Text('Would you like to do a Fast Fourier Transform, or an Inverse Fast Fourier Transform?: ')],
                [sg.Button("Coefficent -> Value  (FFT)", button_color=("white", "blue")),sg.Button("Value -> Coefficient  (IFFT)", button_color=("white", "brown"))]
    ]
    window = sg.Window("Fast Fourier Transform SimpleMade").Layout(layout)
    fft_or_ifft = True
    cont = True
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            cont = False
            break
        if event == "Coefficent -> Value  (FFT)":
            fft_or_ifft = True
            break
        if event == "Value -> Coefficient  (IFFT)":
            fft_or_ifft = False
            break
        
    window.close()  

    if cont == True: #if the user didn't close the window
        if fft_or_ifft == True: # do regular fast fourier transform
            sg.theme('BrightColors')
            layout = [  [sg.Text('Enter in you coefficent list as comma seperate values (and please make its length a power of 2! you can pad with zeros if needed): '), sg.InputText()],
                        [sg.Button("Submit", button_color=("white", "blue"))],
                        [sg.Text("", size = (45,1), key = '-LEN-')]
            ]
            window = sg.Window("Fast Fourier Transform SimpleMade").Layout(layout)
            result = []
            cont = True
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    cont = False
                    break
                if event == "Submit":
                    window['-LEN-'].Update('Running funcion...')
                    window.Refresh()
                    temp = list(map(lambda x: int(x), values[0].split(",")))
                    result = FFT.FastFourierTransform(temp)
                    cont = True
                    break
            window.close()

            strForG = "{ "
            for i,x in enumerate(result):
                strForG += str(x).replace('I',"i")
                if(i!=len(result)-1):
                    strForG += ",  "
                else:
                    strForG += " }"

            if cont == True: #if the user didn't close the window
                sg.theme('BrightColors')
                layout = [  [sg.Text('Okay! The Fast Fourier Function has been run!')],
                            [sg.Text(strForG,font=equation_font) ]
                ]
                window = sg.Window("Fast Fourier Transform SimpleMade").Layout(layout)
                result = []
                cont = True
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        cont = False
                        break
                window.close()

        else: # do inverse fast fourier transform
            sg.theme('BrightColors')
            layout = [  [sg.Text('Enter in you value list as comma seperate values (and please make its length a power of 2! you can pad with zeros if needed): '), sg.InputText()],
                        [sg.Button("Submit", button_color=("white", "blue"))],
                        [sg.Text("", size = (45,1), key = '-LEN-')]
            ]
            window = sg.Window("Fast Fourier Transform SimpleMade").Layout(layout)
            result = []
            cont = True
            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    cont = False
                    break
                if event == "Submit":
                    window['-LEN-'].Update('Running funcion...')
                    window.Refresh()
                    temp = list(map(lambda x: int(x), values[0].split(",")))
                    result = FFT.InverseFastFourierTransform(temp)
                    cont = True
                    break
            window.close()

            strForG = "{ "
            for i,x in enumerate(result):
                strForG += str(x).replace('I',"i")
                if(i!=len(result)-1):
                    strForG += ",  "
                else:
                    strForG += " }"

            if cont == True: #if the user didn't close the window
                sg.theme('BrightColors')
                layout = [  [sg.Text('Okay! The Inverse Fast Fourier Function has been run!')],
                            [sg.Text(strForG,font=equation_font) ]
                ]
                window = sg.Window("Fast Fourier Transform SimpleMade").Layout(layout)
                result = []
                cont = True
                while True:
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        cont = False
                        break
                window.close()


if __name__ == "__main__":
    main()