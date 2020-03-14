import sys
import os
import datetime
import time
import glob

def GetLocalTime():
  """ get local time """
  now_stamp = time.time()
  local_time = datetime.datetime.fromtimestamp(now_stamp)
  return local_time

def UTC2Local(utc_st):
    """UTC to local（+8: 00）"""
    local_time =  GetLocalTime()
    now_stamp = time.mktime(local_time.timetuple())
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


def Local2UTC(local_st):
    """local time to UTC time（-8: 00）"""
    time_stamp = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_stamp)
    return utc_st

def GetDateText():
  """ get now local date text"""
  # print(time.asctime(time.localtime(time.time())))
  local_time = GetLocalTime()
  # print(local_time)
  # print(utc_time)
  local_format = "%Y-%m-%d"
  return time.strftime(local_format, local_time.timetuple())

def GetUTCTimeText():
  """ get now UTC time text"""
  # print(time.asctime(time.localtime(time.time())))
  # local_time = GetLocalTime()
  utc_time = Local2UTC(GetLocalTime())
  # print(local_time)
  # print(utc_time)
  # local_format = "%Y-%m-%dT%H:%M:%S+08:00"
  utc_format = "%Y-%m-%dT%H:%M:%S-08:00"
  # print(time.strftime(local_format, local_time.timetuple()))
  # print(time.strftime(utc_format, utc_time.timetuple()))
  return time.strftime(utc_format, utc_time.timetuple())

def printHelp():
  print("-h: print this help text")
  print("-pt: print UTC time")
  print("-t: title(NECESSARY). Each single word seperate by '_', e.g. -t Test_Title")
  print("-T: template chose, defined template: EF-GL, Music, Notes. e.g. -T EF-GL")
  print("please input one of following template names(the name abbreviation in brackets):")
  print("  Anime(A)")
  print("  Notes(N)")
  print("-c: categories, seperate by comma. e.g. -c EF-GL,English")
  print("-tg: tags, seperate by comma. e.g. -tg EnglishLearning, Advanced")

def GetBlogBaseDataFromArgv(argv):
  nPara = len(argv)
  if nPara < 2:
    printHelp()
    return
  index = 1 # 0 is the file name: new.py
  blogBaseData = {'templateName':'', 'title':'No_title', 'categories':[], 'tags':[], 'extra':''}
  while index < nPara:
    if '-T' == argv[index]: # template commond
      index +=1
      if index >= nPara:
        print("InputErro: Please input the template name after -T")
        return 
      else:
        blogBaseData['templateName'] = argv[index]
    elif '-t' == argv[index]: # title
      index +=1
      if index >= nPara:
        print("InputErro: Please input blog title text after -t")
        return
      else:
        blogBaseData['title'] = argv[index]
    elif '-e' == argv[index]: # extra
      index +=1
      if index >= nPara:
        print("InputErro: Please input blog title text after -e")
        return
      else:
        blogBaseData['extra'] = argv[index]
    elif '-c' == argv[index]: # catefories
        index +=1
        if index >= nPara:
          print("InputErro: Please input blog categories text after -c, each one seperate by comma.")
          return
        else:
          blogBaseData['categories'] = argv[index].split(',')
    elif '-tg' == argv[index]: # tags
      index +=1
      if index >= nPara:
        print("InputErro: Please input blog tags text after -tg, each one seperate by comma.")
        return
      else:
        blogBaseData['tags'] = argv[index].split(',')
    elif '-pt' == argv[index]: ## print UTC time
      index +=1
      print(GetUTCTimeText())
    else:
      print("InputErro: Please input right commond(can't contain space in each part):")
      printHelp()
      return 
    index +=1

  if blogBaseData['title'] == '': # check title
    print("InputErro: Please input blog title text after -t, otherwise the title will be default title: No_title")

  return blogBaseData

def modifyBlogBaseDataByTemplate(blogBaseData):
  if blogBaseData['templateName'] == 'Anime' or blogBaseData['templateName'] == 'A': ## Anime
    if not ('动漫' in blogBaseData['categories']):
      blogBaseData['categories'].append('动漫')
    if not ('剧情设计' in blogBaseData['tags']):
      blogBaseData['tags'].append('剧情设计')
    if not ('故事主题' in blogBaseData['tags']):
      blogBaseData['tags'].append('故事主题')
    ## extra content
    blogBaseData['extra'] += '> \n<!--more-->\n\n'
    blogBaseData['extra'] += '## TV动画\n-------------\n### 角色声优\n\n\n'
    blogBaseData['extra'] += '### 制作人员\n\n\n'
    blogBaseData['extra'] += '### 个人评论\n\n\n'
  elif blogBaseData['templateName'] == 'Notes' or blogBaseData['templateName'] == 'N': ## Notes
    if not ('Notes' in blogBaseData['categories']):
      blogBaseData['categories'].append('Notes')
    if not ('Notes' in blogBaseData['tags']):
      blogBaseData['tags'].append('Notes')
  else:
    print("InputErro: Undefined template name")
    print("please input one of following template names(the name abbreviation in brackets):")
    print("  Anime(A)")
    print("  Notes(N)")
    return


def getHeadText(blogBaseData):
  headText='---\n'
  if blogBaseData['templateName'] != '':
    modifyBlogBaseDataByTemplate(blogBaseData) ## modify the base data
  headText+='title: \"'+blogBaseData['title'].replace('_',' ')+'\"\n' ## title line
  headText+='image: \n'
  headText+='  path: /imgs/ \n'
  headText+='  thumbnail: /imgs/ \n'
  ## categories
  headText+='categories:\n'
  for text in blogBaseData['categories']:
    if text != '':
      headText+='  - '+text+'\n'
  ## tages
  headText+='tags:\n'
  for text in blogBaseData['tags']:
    if text != '':
      headText+='  - '+text+'\n'
  ## last modified UTC datetime
  headText+='excerpt_separator: <!--more-->\n'
  headText+='last_modified_at: '+GetUTCTimeText()+'\n'
  headText+='---\n'
  if blogBaseData['extra'] != '':
    headText+=blogBaseData['extra']
  return headText


def main(argv):
  blogBaseData = GetBlogBaseDataFromArgv(argv)
  if blogBaseData == None:
    return
  
  dateText=GetDateText()
  postpath='./_posts/'
  filepath=postpath+dateText+'-'+blogBaseData['title'].replace('_','-')+'.md'
  if os.path.exists(filepath):
    print("The file already exists, do you want to replace(Y/n)")
    YesOrNo=input()
    if YesOrNo != 'Y' and YesOrNo != 'y': # exit if no replace
      return
  if blogBaseData['templateName'] == 'EF_GL' or blogBaseData['templateName'] == 'EG': ## EF_GL
    searchPath = postpath+'*-'+blogBaseData['title'].replace('_','-')+'.md'
    print(searchPath)
    sameFile = glob.glob(searchPath)
    if len(sameFile) == 1:
      print("The same title file of EF Group lesson already exists, do you want to update(Y/n)")
      YesOrNo=input()
      if YesOrNo == 'Y' or YesOrNo == 'y': # exit if no replace
        print(GetUTCTimeText())
        os.rename(sameFile[0],filepath) ## rename file to update the date
        return
    elif len(sameFile) > 1:
      print("The several same topic files of EF Group lesson already exists, please check the follwing files:")
      for index in range(0,len(sameFile)):
        print(str(index)+' : '+sameFile[index]) ## list all files
      print("Do you want to update one of them, please in put the index(-1 means no update):")
      updateIndex = int(input())
      if updateIndex < len(sameFile)-1 and updateIndex >= 0:
        print(GetUTCTimeText())
        os.rename(sameFile[updateIndex],filepath) ## rename file to update the date
        return
  postfile=open(filepath,'w',encoding='utf-8')
  headText=getHeadText(blogBaseData)
  postfile.write(headText)
  postfile.close

  print('new post successed: '+filepath)
  print('title: '+blogBaseData['title'])

if __name__ == "__main__":
    main(sys.argv)