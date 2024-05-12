import os
import sys


AllowAudioFormat = {'mp3','aac','flac'}
AllowVideoFormat = {'flv','mp4','mkv'}
SourceFormat = ''
TargetFormat = ''

def to_flac(file_dir):
  save_dir = file_dir.replace(SourceFormat, TargetFormat)
  cmd = 'ffmpeg -i ' + '"'+file_dir+'" ' + '-vn -compression_level 12 ' + '"'+save_dir +'"'
  # print(cmd)
  os.system(cmd)

# 遞歸訪問目錄，回傳最底层文件绝对路径的列表
def check_file(file_path):
    os.chdir(file_path)
    print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(os.path.join(file_path,f)))
            os.chdir(file_path)
        else:
            files.append(os.path.abspath(f))
    return files

def format_check():
  global SourceFormat,TargetFormat
  SourceFormat = input('Please input input format: ')
  TargetFormat = input('Please input Ouput format: ')

  if(TargetFormat in AllowAudioFormat):
      TargetFormat = '.'+TargetFormat
  else:
    print('Invalid Output format: ',TargetFormat)
    print('Allowed Format:',AllowAudioFormat)
    sys.exit()
  
  if(SourceFormat in AllowVideoFormat):
    SourceFormat = '.'+SourceFormat
  else:
    print('Invalid Input format: ',SourceFormat)
    print('Allowed Format:',AllowVideoFormat)
    sys.exit()

  if(SourceFormat == TargetFormat):
    print('Seriously ? Output format equals to Input format !')
    sys.exit()


    
if __name__ == "__main__":
  workingDir = os.getcwd()
  WorkingList = check_file(workingDir)

  format_check()

  for filename in WorkingList:
    if filename.endswith(SourceFormat):
      print("Found " + filename)
      to_flac(filename)
      print(filename + " Convert Complete !")

  print("All Done !")