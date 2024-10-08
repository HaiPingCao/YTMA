import os

options:dict = {
     'no_warnings': True,
     'ignoreerrors': True,
     'quiet': True,
     'verbose': False,

     'abort_on_unavailable_fragments': True,
     'keepvideo': False,

     'flat_list': False,
     'noplaylist': False,
}

def opts(mode:int, playlist:bool, debug:bool, download_folder:str = "\\Temp"):
     modified_options = options.copy()
     # PLAYLIST ?
     if playlist == False:
          modified_options.update({
               'flat_list': True,
               'noplaylist': True
               })
     # DEBUG
     if debug == True:
          modified_options.update({
               'no_warnings': False,
               'ignoreerrors': False,
               'quiet': False,
               'verbose': True
          })
     # MP3 DOWNLOAD
     # elif mode == 1:
     #      modified_options['format'] = 'bestaudio/best'
     #      modified_options['outtmpl'] = os.path.join(download_folder, '%(title)s.%(ext)s')
          modified_options['postprocessors']=[{
               'key': 'FFmpegExtractAudio',
               'preferredcodec': 'mp3',
               'preferredquality': '192',
          }]
     #MP3 STREAM / INFO
     elif mode == 2:
          pass
     return modified_options

if __name__ == '__main__':
     print(f'\n{options}\n')
     fn = opts(mode=1, playlist=False, debug=True)
     print(fn)