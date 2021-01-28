set fname=%1
shift
cd video
copy /b *.ts %fname%.mp4

del /S /Q *.ts