<div align="center" style="text-align: center">

<p style="text-align: center">
  <img align="center" src="efisherylogolandscape.jpg" alt="eFishery" width="500">
</p>

</div>

# eFishery Task 3 - Vibrio Detection
<p> Hi.. </p>
The purpose of this project is to be able detect, counting, and classifying vibrio bacteria with YOLOv8, well known as one of the DeepLearning object detection algorithm.
This is also part of take home test for applying Machine Learning Computer Vision Engineer in eFishery.

---
## Problem
Mr. Joshua who is an Aquaculture Expert in the field of microbiology. At this time, he is in need of help to count the number of vibrio colonies because he is used to processing more or less 100 cups per day. Counting one cups consist dozens of different vibrio already a pain, imagine 100 cups. 
Mr. Joshua need an alternative or automatic ways to do this painfull jobs.
Hello and welcome.. 
Aim of this project is to be able detect, counting, and classifying vibrio bacteria with YOLOv8, well known as one of the DeepLearning object detection algorithm.
This is also part of take home test for applying Machine Learning Computer Vision Engineer in eFishery.

## Idea

  
## Solution
To make Mr. Joshua live easier, we create a web based platform to be able detect vibrio, classify & count.
Deep learning approach were made to solved this problem, by using YOLOv8 (You Only Look Once version 8) we be able to detect, classify the size also color of the vibrio.

  How it work
  1. Prepare the dataset, annotate the image, and export it into YOLOv8 format (I used Roboflow to do this).
  2. Train the pretrained models of YOLOv8 with our dataset (link train.ipynb).
  3. Use ClearML to tracks and controls the process, performance metrics, and model storing.
  4. Create the platform using streamlit and inference the image using the our trained model.
  

To make it easier to make a solution, he provides a sample of 20 petri dish images on this link with an area of 7854 mm , which are observations of vibrio species on pond water quality

## Solusi
Berdasarkan permasalahan yang disebutkan yaitu untuk membantu "Menghitung jumlah spesies vibrio dengan warna yang berbeda dan mengukur size dari tiap species yang terdapat pada gambar tersebut. Untuk mensolve problem tersebut diperlukan platform untuk mempermudah beliau melakukan ekstraksi ukuran dan warna dari tiap koloni vibrio". 


## Installation and Usage
Berikut adalah langkah-langkah untuk menginstal dan menjalankan proyek ini di local environtment, sangat disarankan untuk menggunakan virtual environment atau sudah terpasang docker:
### PYTHON USAGE
1. Clone this git repo, you can download or use commmand below
```
git clone https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery.git
```
2. Install depedency (Recommend to create Virtual Environtment first before doing this step)
   Enter the project directory then run this command in CLI like CMD:
```
pip install -r requirements.txt
```
4. To run the program, just run this command
```
streamlit run app.py
```
5. Browser will automatically open, if not, type localhost:8501 to broweser address. Web application page will be open.

### DOCKER COMPOSE
1. Kloning repositori ini: Gunakan perintah git clone untuk mengkloning repositori ini ke direktori lokal.
```
git clone https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery.git
```
2. Jalankan perintah `docker-compose` ini untuk mulai build dan menjalankan langsung aplikasi
```
docker-compose up
```
3. Buka browser internet dan masuk ke localhost:8501, aplikasi terbuka selamat mencoba.

## Interface antar muka
### Input gambar
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/9dea2503-535f-41e3-bb46-01db01686667)
### Upload Gambar
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/3899a2d9-a9fe-4bc0-b627-d0f1a9c33d66)
### Hasil deteksi dan Perhitungan
![image](https://github.com/fulankun1412/Vibrio-YOLOv8-Lanang-eFishery/assets/16248869/08175c0a-2a99-46d4-8176-a72b9e5da08e)
