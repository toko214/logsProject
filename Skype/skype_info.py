"""
author: Tomer Perets
date: 5.5.2018
this file contains functions that help get data from skype,
messages, contacts, users.
"""


import os
import usefull_things as ut
from lxml import html

folder_list = ['Content', 'DataRv', 'logs', 'My Skype Received Files', 'RootTools', 'shared_httpfe', 'SkypeRT']
folder_list2 = ['coexistence', 'DataRv', 'DiagOutputDir', 'logs', 'SkypeRT','Tracing','Avatar']
PATH = []

MESSAGE_REMOVED_TEXT = "This message has been removed."
MESSAGES_TYPE_TOPIC = 2# Changed chat topic or picture
MESSAGES_TYPE_GROUP        =   4 # Created group conversation
MESSAGES_TYPE_PARTICIPANTS =  10 # Added participants to chat
MESSAGES_TYPE_REMOVE       =  12 # Removed participants from chat
MESSAGES_TYPE_LEAVE        =  13 # Contact left the chat
MESSAGES_TYPE_CALL         =  30 # Started Skype call
MESSAGES_TYPE_CALL_END     =  39 # Skype call ended
MESSAGES_TYPE_SHARE_DETAIL =  51 # Sharing contact details
MESSAGES_TYPE_MESSAGE      =  61 # Ordinary message
MESSAGES_TYPE_CONTACTS     =  63 # Sent contacts
MESSAGES_TYPE_SMS          =  64 # SMS message
MESSAGES_TYPE_FILE         =  68 # File transfer
MESSAGES_TYPE_BIRTHDAY     = 110 # Birthday notification
TRANSFER_TYPE_OUTBOUND     =   1 # An outbound transfer, sent by this account
TRANSFER_TYPE_INBOUND      =   2 # An inbound transfer, sent to this account

def path_1(appdata_path):
    """
    searching for the %appdata%\Roaming\Skype\user\main.db kind of path
    :param appdata_path: the appdata path
    :return: setting a path var
    :return: error  number
    """
    data_path = appdata_path+"\Roaming\Skype"
    if os.path.exists(data_path):
        folders = next(os.walk(data_path))[1]
        for i in folder_list:
            if i in folders:
                folders.remove(i)
        if folders == []:
            return
        for i in folders:
            sqlite3_path = data_path + "\\" + i + "\main.db"
            PATH.append([1,sqlite3_path])

def path_2(appdata_path):
    """
    searching for the %appdata%\Local\Packages\Microsoft.SkypeApp_\LocalState\user\skype.db kind of path
    :param appdata_path: the appdata path
    :return: setting a path var
    :return: error number
    """
    data_path = appdata_path+"\Local\Packages\\"
    folder_list = next(os.walk(data_path))[1]
    skype_folder = ""
    for folder in folder_list:
        if "Microsoft.SkypeApp_" in folder:
            skype_folder = folder
            break
    if skype_folder=="":
        return
    skype_folder = data_path +skype_folder+"\LocalState\\"
    folders = next(os.walk(skype_folder))[1]
    for i in folder_list2:
        if i in folders:
            folders.remove(i)
    if folders == []:
        return
    for i in folders:
        sqlite3_path = skype_folder + i + "\skype.db"
        PATH.append([2,sqlite3_path])

def set_path():
    """
    calling functions that will search in the computer for skype program
    :return: error number
    """
    appdata_path =  os.path.expanduser('~') + "\AppData"
    path_1(appdata_path)
    path_2(appdata_path)

def get_accounts(path):
    """
    searching in the skype database for information on the skype user or users.
    :param path: the path of the skype database file
    :return1: error number
    :return2: skype user information
    """
    select_statement = "SELECT id,skypename,fullname,birthday,gender,languages,country,city,emails,mood_text FROM Accounts"
    select_statement2 = "SELECT key, value FROM key_value"
    cursor = ut.connect_to_sqlite3_db(path[1])
    if path[0] == 1:
        try:
            results = ut.execute_sql(cursor,select_statement)
            if len(results) > 0:
                inner_dict = {}
                inner_dict['username'] = str(results[0][1])
                inner_dict['fullname'] = str(results[0][2])
                inner_dict['birthday'] = str(results[0][3])
                gender = "female"
                if results[0][4] == 1:
                    gender = "male"
                inner_dict['gender'] = gender
                inner_dict['language'] = str(results[0][5])
                inner_dict['country'] = str(results[0][6])
                inner_dict['city'] = str(results[0][7])
                inner_dict['email'] = str(results[0][8])
                inner_dict['mood'] = str(results[0][9])
                return [inner_dict]
            return ['err',1,select_statement]
        except Exception as ex:
            return ['err',13,path[1],ex]
    if path[0] == 2:
        try:
            results = ut.execute_sql(cursor,select_statement2)
            if len(results) > 0:
                inner_dict = {}
                inner_dict['username'] = results[1][1]
                inner_dict['fullname'] = results[2][1]
                inner_dict['mood'] = results[5]
                inner_dict['avatar_url'] = results[6]
                return [inner_dict]
            return ['err',1,select_statement2]
        except Exception as ex:
            return ['err',13,path[1],ex]

def get_contacts(path):
    """
    searching in the skype database for contacts of the skype user or users.
    :param path: the path of the skype database file
    :return1: error number
    :return2: skype users contacts
    """
    select_statement = "SELECT skypename,fullname,birthday,gender,country,city,phone_home,phone_office,phone_mobile,emails,homepage,about,mood_text,avatar_url FROM Contacts"
    select_statement2 = "SELECT mri,full_name,birthday,gender,country,city,assigned_phonenumber_3,assigned_phonenumber_2,assigned_phonenumber_1,phone_number_home,phone_number_office,phone_number_mobile,homepage,about_me,avatar_url,avatar_downloaded_from ,contact_type FROM Contacts"
    Contacts = {}
    cursor = ut.connect_to_sqlite3_db(path[1])
    if path[0] == 1:
        try:
            results = ut.execute_sql(cursor,select_statement)
            if len(results) > 0:
                for contact in results:
                    inner_dict = {}
                    inner_dict['username'] = contact[0]
                    inner_dict['fullname'] = contact[1]
                    if contact[2] != None:
                        inner_dict['birthday'] = str(contact[2])[:4] + "/" + str(contact[2])[4:6] +"/" +str(contact[2])[6:]
                    else:
                        inner_dict['birthday'] = "Never Borned"
                    gender = 'female'
                    if contact[3] == 1:
                        gender = "male"
                    inner_dict['gender'] = gender
                    inner_dict['country'] = contact[4]
                    inner_dict['city'] = contact[5]
                    inner_dict['phones'] = [contact[6],contact[7], contact[8]]
                    inner_dict['email'] = contact[9]
                    inner_dict['realeted_urls'] = [contact[10],contact[11],contact[12]]
                    inner_dict['avatar_profile'] = contact[13]
                    Contacts[contact[0]] = inner_dict
                return [Contacts]
            return ['err',1,select_statement]
        except Exception as ex:
            return ['err',13,path[1],ex]

    if path[0] == 2:
        try:
            results = ut.execute_sql(cursor,select_statement2)
            if len(results) > 0:
                for contact in results:
                    if contact[16] == 8:
                        inner_dict = {}
                        skype_name = contact[0]
                        indx = skype_name.find(':')
                        skype_name = skype_name[indx+1:]
                        #inner_dict['username'] = skype_name
                        inner_dict['fullname'] = contact[1]
                        if contact[2] != None:
                            inner_dict['birthday'] = str(contact[2])[:4] + "/" + str(contact[2])[4:6] +"/" +str(contact[2])[6:]
                        else:
                            inner_dict['birthday'] = "Never Borned"
                        gender = 'female'
                        if contact[3] == 1:
                            gender = "male"
                        inner_dict['gender'] = gender
                        inner_dict['country'] = contact[4]
                        inner_dict['city'] = contact[5]
                        inner_dict['phones'] = [contact[6],contact[7], contact[8],contact[9],contact[10],contact[11]]
                        inner_dict['realeted_urls'] = [contact[12],contact[13]]
                        inner_dict['avatar_profile'] = [contact[14],contact[15]]
                        Contacts[skype_name] = inner_dict
                return [Contacts]
            return ['err',1,select_statement2]
        except Exception as ex:
            return ['err',13,path[1],ex]

def get_messages(path):
    #convo type = 19
    #private message = 8
    """
    searching in the skype database for messages that the user got or sent .
    :param path: the path of the skype database file
    :return1: errornumber
    :return2: skype user information
    """
    select_statement1 = "SELECT convo_id , chatname, author, datetime(timestamp + 10800, 'unixepoch') as date,body_xml, type, identities FROM Messages order by convo_id"
    select_statement2 = "SELECT convo_id,identity FROM Participants order by convo_id"
    select_statement3 = "SELECT convdbid,originalarrivaltime ,editedtime ,content,author, messagetype FROM messages order by convdbid"
    select_statement4 = "SELECT dbid,type,id,thread_admins FROM conversations order by dbid "
    cursor = ut.connect_to_sqlite3_db(path[1])
    MESSAGES = {}
    if path[0] == 1:
        try:
            results = ut.execute_sql(cursor,select_statement1)
            results2 = ut.execute_sql(cursor,select_statement2)
            if len(results) > 0:
                for message in results:
                    if not message[0] in MESSAGES:
                        inner_dict = {}
                        inner_dict['group'] = "No"
                        inner_dict['participatins'] = " "
                        m_from = message[2]
                        to_remove = []
                        temp = None
                        count = 0
                        for parti in results2:
                            if parti[0] == message[0] and parti[1]!=m_from:
                                count += 1
                                inner_dict['participatins'] += parti[1] + ", "
                                to_remove.append(parti)
                                temp=parti[1]
                            else:
                                if temp!=None:
                                    break
                        if count > 1:
                            inner_dict['group'] = "Yes"
                        inner_dict['participatins'] += m_from #inner_dict['participatins'][:-2]
                        for i in to_remove:
                            results2.remove(i)
                        msg = message[4]
                        if '<a href' == str(msg)[:7]:
                            msg = html.fromstring(str(msg))
                            msg = msg.xpath('//a/@href')
                            msg = msg[0]
                        elif message[5] == MESSAGES_TYPE_CALL:
                            msg = "Call Started With: " + message[6]
                        elif message[5] == MESSAGES_TYPE_CALL_END:
                            msg = "Call Ended With: " + message[6]
                        elif message[5] == MESSAGES_TYPE_PARTICIPANTS:
                            msg = m_from + " Added " + message[6]
                        elif message[5] == MESSAGES_TYPE_REMOVE:
                            msg = m_from + " Removed " + message[6]
                        inner_dict['messages'] = [{'time':message[3],'message':msg,'from':m_from}]
                        MESSAGES[message[0]] = inner_dict
                    else:
                        m_from = message[2]
                        msg = message[4]
                        if '<a href' == str(msg)[:7]:
                            msg = html.fromstring(str(msg))
                            msg = msg.xpath('//a/@href')
                            msg = msg[0]
                        elif message[5] == MESSAGES_TYPE_CALL:
                            msg = "Call Started"
                        elif message[5] == MESSAGES_TYPE_CALL_END:
                            msg = "Call Ended"
                        elif message[5] == MESSAGES_TYPE_MESSAGE:
                            msg = message[4]
                        elif message[5] == MESSAGES_TYPE_PARTICIPANTS:
                            msg = m_from + " Added " + message[6]
                        elif message[5] == MESSAGES_TYPE_REMOVE:
                            msg = m_from + " Removed " + message[6]
                        MESSAGES[message[0]]['messages'].append({'time':message[3],'message':msg,'from':message[2]})
                return [MESSAGES]
            return ['err',1, select_statement1]
        except Exception as ex:
            return ['err',13, path[1],ex]
    if path[0] == 2:
        try:
            results = ut.execute_sql(cursor,select_statement3)
            results2 = ut.execute_sql(cursor,select_statement4)
            if len(results) > 0:
                for message in results:
                    if not message[0] in MESSAGES:
                        inner_dict = {}
                        indx = message[4].find(":")
                        m_from = message[4][indx+1:]
                        for parti in results2:
                            if parti[0] == message[0]:
                                if parti[1] == '8':
                                    inner_dict['group'] = "No"
                                    inner_dict['participatins'] = [m_from,parti[3]]
                                    results2.remove(parti)
                                    break
                                if parti[1] == '19':
                                    inner_dict['group'] = "Yes"
                                    if parti[3]:
                                        partis = parti[3].replace('8:','').split(' ')
                                    else:
                                        partis = ""
                                    inner_dict['participatins'] = partis
                                    results2.remove(parti)
                                    break
                        msg = message[3]
                        if message[5] == 10:
                            msg = "Call Ended/Started"
                        inner_dict['group'] = "Yes"
                        inner_dict['messages'] = [{'edit_time':message[2],'time':message[1],'message':msg,'from':m_from}]
                        MESSAGES[message[0]] = inner_dict
                    else:
                        msg = message[3]
                        if message[5] == 10:
                            msg = "Call Ended/Started"
                        indx = message[4].find(":")
                        m_from = message[4][indx+1:]
                        MESSAGES[message[0]]['messages'].append({'edit_time':message[2],'time':message[1],'message':msg,'from':m_from})
                return [MESSAGES]
            return ['err',1,select_statement1]
        except Exception as ex:
            print ex
            return ['err',13, path[1],ex]
set_path()

