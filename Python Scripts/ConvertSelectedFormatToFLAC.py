import os
import sys

SourceFormat = ''  # '.wav' # '.flv'
TargetFormat = '.flac'


def ConvertBy_ffmpeg(file_dir):
    save_dir = file_dir.replace(SourceFormat, TargetFormat)
    cmd = f'ffmpeg -i "{file_dir}" -f {TargetFormat}  -ar 16000 -ac 1 "{save_dir}" > nul'
    # print(cmd)
    result =os.system(cmd)
    return result

# 遞歸訪問目錄，回傳最底层文件绝对路径的列表


def check_file(file_path):
    os.chdir(file_path)  # 改變當前工作路徑為指定路徑
    print(os.path.abspath(os.curdir))
    all_file = os.listdir()
    files = []
    for f in all_file:
        if os.path.isdir(f):
            files.extend(check_file(os.path.join(file_path, f)))
            os.chdir(file_path)
        else:
            files.append(os.path.abspath(f))
    return files


if __name__ == "__main__":
  workingDir = os.getcwd()
  WorkingList = check_file(workingDir)

  SourceFormat = input('Please input the Source format: ')
  TargetFormat = input('Please input the Target format: ')

  # if(SourceFormat != 'flv' and SourceFormat != 'wav' and SourceFormat !='mp3'):
  #   print('Invalid Source Format:',SourceFormat)
  #   print('Valid Format: flv, wav, mp3')
  #   sys.exit()
  # else:

  for filename in WorkingList:
    if filename.endswith(SourceFormat):
      # print("Found " + filename)
      # convertlist.append(workingDir+filename)
      if ConvertBy_ffmpeg(filename) != 0: exit(-1)
      print(filename + " Convert Complete !")
      # converted_count += 1
    # else:
    #   print("Not wav file : " + filename)

  print("All Done !")

  # for file in convertlist:
  #   if file.split('.')[-1] == 'wav':
  #     wav_ConvertBy_ffmpeg(file)
  #     print("Done" + filename)
