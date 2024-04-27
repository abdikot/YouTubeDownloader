# import yang diperlukan
import customtkinter as ctk     #import GUI customtkinter menjadi ctk
from tkinter import ttk         #import GUI 
from pytube import YouTube      #import aksses YouTube
import os                       #import OS

def download_video():   # Metode download_video
    url = entry_url.get()   #mengambil nilai dari entry_url dan disimpan di variabel url
    resolution = resolutions_var.get()  # mengambil nilai dari resolution_var dan disimpan di variabel resolution

    progress_label.pack(pady="10p", padx="10p") # menampilkan progress_label di GUI
    progress_bar.pack(pady="10p", padx="10p")   #menampilkan progress_bar di GUI
    status_label.pack(pady="10p", padx="10p")   #menampilkan status_label di GUI

    try: # mencoba untuk mendownload video
        yt = YouTube(url, on_progress_callback=on_progress)  # membuat objek YouTube dengan URL dan callback on_progress  || on_progress_callback digunakan untuk memberitahu kemajuan pengunduhan
        stream = yt.streams.filter(res=resolution).first()  # filter resolusi video yg akan didownload

        os.path.join("downloads", f"(yt.title).mp4")  # membuat nama file berdasarkan judul video dengan ekstens
        stream.download(output_path="downloads")  # memulai proses download dengan informasi path dan resolusi

        status_label.configure(text="Downloaded", text_color="white", fg_color="green") #konfigurasi status_label dengan warna hijau jika download berhasil berhasil
    except Exception as e:   # jika terjadi error, maka akan dilakukan except
        status_label.configure(text=f"error {str(e)}", text_color="white", fg_color="red") #jika terjadi error status label akan berwarna merah dan menampilkan pesan error yang terjadi

def on_progress(stream, chunk, bytes_remaining): #metode yang digunakan untuk memperlihatkan progress download
    total_size = stream.filesize            # .filesize mengambil ukuran file video dan disimpan di total_size
    bytes_downloaded = total_size - bytes_remaining # menghitung ukuran yang sudah terunduh dengan cara mengurangi total_size(ukuran file) dengan sisa yang belum diunduh dan nilainya disimpan di bytes_download
    percentage_completed = bytes_downloaded / total_size * 100 #menghitung  persentase yang sudah terunduh dengan cara membagi data yang sudah terunduh(bytes_downloaded) dengan ukuran file(total_size) lalu dikali 100 dan nilainya disimpan di percentage_completed 
    
    progress_label.configure(text = str(int(percentage_completed)) + "%") #.configure mengkonfigurasi progress_label dengan mengambil nilai dari percentage_completed || str(int(percentage_completed)) ,mengubah nilai dari percentage_completed menjadi integer lalu diubah lagi menjadi string
    progress_label.update()   # memperbarui label progress_label dengan informasi tentang proses download

    progress_bar.set(float(percentage_completed / 100))    #memperbarui progress bar dengan persentase yang sudah selesai


root = ctk.CTk()    #mendefinisikan root
ctk.set_appearance_mode("System")   # .set_appearance_mode mengubah tema utama GUI menjadi ("system") default
ctk.set_default_color_theme("blue") # .setdefault_color_theme mengubah warna utama GUI menjadi ("blue")

root.title("Youtube Downloader")    # .title mengubah judul dari GUI

root.geometry("720x480")    # .geometry mengubah skala besar kecil GUI 
root.minsize(720, 480)      # .minisize mengubah skala minimal GUI
root.maxsize(1080, 720)     # .maxisize mengubah skala maximal GUI

content_frame = ctk.CTkFrame(root)  #. CTkFrame membuat frame baru
content_frame.pack(fill=ctk.BOTH, expand=True, padx="10p", pady="10p")    # .pack mengatur tata letak frame || fill=ctk.BOTH mengisi ruang yang tersedia baik horizontal maupun vertikal || expand=True membuat frame memperluas dirinya sesuai dengan ruang yang ada || padx dan pady mengisi padding di frame

label_url = ctk.CTkLabel(content_frame, text="Masukan Link Video YouTube Disini : ")  #.CTkLabel membuat label || (content_frame,...) membuat CTkLabel berada di dalam variabel content_frame(di dalam frame)
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)   # .CTkEntry membuat Text Field ||  (content_frame,...) membuat CTkLabel berada di dalam variabel content_frame(di dalam frame)
label_url.pack(padx="10p", pady="10p")  # menambahkan padding ke label_url
entry_url.pack(padx="10p", pady="10p")  # menambahkan padding ke entry_url

download_url = ctk.CTkButton(content_frame, text="Download", command=download_video) # .CtkButton membuat button || command adalah action yang akan terjadi jika button di clik (dicontoh ini menjalankan metode download_video)
download_url.pack(padx="10p", pady="10p")   # menambahkan padding 

resolutions = ["720p", "480p", "360p"]  #membuat variabel resolution dengan tipe data array 
resolutions_var = ctk.StringVar()   # tempat menyimpan variabel yang didapat dari resolution_combobox
resolutions_combobox = ttk.Combobox(content_frame, values=resolutions , textvariable=resolutions_var )  #combobox dengan nilai resolution yang nilainya disimpan diresolution_var
resolutions_combobox.pack(padx="10p", pady="10p")# menambahkan padding ke entry_url
resolutions_combobox.set("720p") # mengubah tampilan awal combobox agar memilih 720p

progress_label = ctk.CTkLabel(content_frame, text="0%") #.CTkLabel membuat label

progress_bar = ctk.CTkProgressBar(content_frame, width=400) #membuat progressbar  dengan lebar 400 pixel 
progress_bar.set(0.6) #mengubah nilai awal dari progressbar menjadi  0.6 (60%)

status_label = ctk.CTkLabel(content_frame, text="Succses")  #.CTkLabel membuat label dan memberi tanda sukses

root.mainloop() #.mainloop menjalankan GUI