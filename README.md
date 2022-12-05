# MS-F22-ML-Project
This repository is for Machine Learning course project at Innopolis University Fall 2022

The goal of this project is to run an optimized version of Yolov7 on Raspberry Pi 4.

## System setup
- Raspberry Pi 4 8GB Ram
- Raspberry OS 64
- Python 3.9
- Webcam
- Heat sink and fans for cooling
## System configurations
There is a script to run the code on startup so we don't have to run the code everytime the PI restart.

The code intialize a flask server to have access to the models not only form the PI but from any computer in the network, this can allow us to run the PI in headless mode wich can increase the FPS by ~1FPS.

There is an option for multiprocessing that theoritically can increase performance. However, after testing it, it turns out that it gives less FPS because the PI CPU usage increases to 100%.

## Base line
After running Yolov5 nano on the PI the average FPS was ~0.33, even with overclocking(makes the PI unstable) the FPS was ~0.5

 
![screen-gif](./Yolov5n-output.gif)

## ONNX
After compiling Yolo with ONNx, the FPs increase to ~2.2FPS, which is more the 6x increase in performance
![screen-gif](./Yolov7n-output.gif)

## How to run

link to the models:
https://drive.google.com/file/d/1j2_oH5rFfYDcFJmgQF7z723M7aT4C0sD/view?usp=sharing

extract the models in the 'models' directory

## To automate the script to run on startup
- open the terminal
- run this command to make the `.sh` execurable: `chmod +x run.sh`
- run `crontab -e` to open the cron file
- add this to the file `@reboot <path to run.sh>`: put the abslute path of run.sh.
it should look somthing like `@reboot /home/pi/Desktop/Yolo-Rasbperry-pi/run.sh`
- save and exit


For the multiprocess code do the same steps as above, but instead of using `run.sh` use `mp_run.sh`

Note: the multiprocess code runs without the need to have the web streem open.
it even runs faster that the normal code when the web streem is closed.
On the other hand, when the web streem is open it runs slower because the overhead
of the inter process communication 


## custom models
To use a custom model, creat a directory called `custom` and add you models to it
the name of the model has to contain it's type (i.e. if the model is a yolov5
version then 'tolov5' has to be in the name).

Then restart the code to see the effect
