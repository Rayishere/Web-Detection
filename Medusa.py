#!/usr/bin/python
#coding:utf-8
import urllib2
import hashlib
import time

def usage():
    print("=" * 60)

isTag = 'b7cd44d91dc839f2648b1eadabc5423f'
isWebContent = '5452fac71ebac14b9929755ed6327f03'
isTagattributes = '6d65f709165d39e3fed79797eb8f5780'
isTagcontent = 'c479525739fecb38967aba0c3b424228'

req = urllib2.Request('http://www.cgu.edu.tw/')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')

while 1:
    html_doc = urllib2.urlopen(req).read()
    #html_doc = '''<html><head></head></html>'''

    isStart = False
    isContent = False
    #tag end not content
    isNotContent = False
    isEnd = False
    isNotEnd = True

    html_tag_attributes = ''
    html_tag_attributes_list = []

    html_tag = ''
    html_tag_list = []

    html_content = ''
    html_content_list = []

    html_tag_content = ''
    html_tag_content_list = []

    html_doc_word = len(html_doc)
    word_number = 0
    #Web Contetn Capcut ------
    for tmp in html_doc:
        if isEnd:
            if tmp == '"' or tmp == "'":
                isNotEnd = not(isNotEnd)
            if isNotEnd and tmp == '>':
                html_tag_attributes_list.append(html_tag_attributes)
                html_tag_attributes = ''
                isContent = not(isContent)
                isEnd = not(isEnd)
            else:
                html_tag_attributes = html_tag_attributes + tmp

        if isStart:
            if tmp is ' ':
                html_tag_list.append(html_tag)
                html_tag = ''
                isStart = not(isStart)
                isEnd = not(isEnd)
            elif tmp == '/' or tmp == '!':
                if tmp == '/':
                    isNotContent = not(isNotContent)
                isStart = not(isStart)
                html_tag = ''
            elif tmp == '>':
                html_tag_list.append(html_tag)
                html_tag = ''
                isContent = not(isContent)
                isStart = not(isStart)
            else:
                html_tag = html_tag + tmp

        if tmp is '<':
            if isContent:
                html_content_list.append(html_content)
                html_content = ''
                isContent = not(isContent)
            isStart = not(isStart)

        if isContent and tmp != '>':
            html_content = html_content + tmp
        
        if not(isStart) and not(isEnd) and not(isContent):
            if not(isNotContent):
                html_tag_content = html_tag_content + tmp
            if tmp == '>':
                isNotContent = not(isNotContent)
            if html_doc_word == (word_number+1):
                if html_tag_content != '':
                    html_tag_content_list.append(html_tag_content)
                    html_tag_content = ''
        else:
            if html_tag_content != '':
                html_tag_content_list.append(html_tag_content)
                html_tag_content = ''

        word_number = word_number + 1
    #Web Contetn Capcut ------

    #print html_tag_list
    #break
    #rint html_content_list
    #print html_tag_attributes_list
    #print html_tag_content_list

    #print hashlib.md5(str(html_tag_list).decode('string_escape')).hexdigest()
    #print hashlib.md5(str(html_content_list).decode('string_escape')).hexdigest()
    #print hashlib.md5(str(html_tag_attributes_list).decode('string_escape')).hexdigest()
    #print hashlib.md5(str(html_tag_content_list).decode('string_escape')).hexdigest()

    #print '='*50
    print time.strftime("%m %d %H:%M:%S %Y", time.localtime())
    print '='*50
    if isTag != hashlib.md5(str(html_tag_list).decode('string_escape')).hexdigest():
        print 'tag = Error'
    else:
        print 'tag = Success'
    print '='*50
    if isWebContent != hashlib.md5(str(html_content_list).decode('string_escape')).hexdigest():
        print 'content = Error'
    else:
        print 'content = Success'
    print '='*50
    if isTagattributes != hashlib.md5(str(html_tag_attributes_list).decode('string_escape')).hexdigest():
        print 'tag attributes = Error'
    else:
        print 'tag attributes = Success'
    print '='*50
    if isTagcontent != hashlib.md5(str(html_tag_content_list).decode('string_escape')).hexdigest():
        print 'tag content = Error'
    else:
        print 'tag content = Success'
    print '='*50
    time.sleep(300)