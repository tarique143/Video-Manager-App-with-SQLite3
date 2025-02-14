import sqlite3
conn=sqlite3.connect('video_manager.db')
cursor=conn.cursor()
cursor.execute('''
create table if not exists videos(
        id integer Primary key,
               name text not null,
               time text not null
               
                )
''')
def  listVideos():
    cursor.execute("select * from videos")
    for row in cursor.fetchall():
        print(row)
    
def  add_video(name,time):
    cursor.execute("insert into videos (name,time) values(?, ?)",(name,time))
    conn.commit()
    
def update_video(video_id,name,time):
    cursor.execute("update videos set name=?,time=? where id=?",(name,time,video_id))
    conn.commit()
def delete_video(id):
    cursor.execute('delete from videos where id=?',(id,))
    conn.commit()

def main():
    while True:

        print("YOUTUBE MANAGER APP WITH DB")
        print("1. LIST VIDEOS")
        print("2. ADD VIDEOS")
        print("3. UPDATE VIDEOS")
        print("4.DELETE VIDEOS")
        print("5. EXIT")
        #print("")
        choice=input("Entet your choices: ")
        if choice=='1':
            listVideos()
        elif choice=='2':
            name=input("Enter the video name: " )
            time=input("Enter the video Time: " )
            add_video(name,time)
        elif choice=='3':
            video_id=input("Enter video id to update: ")
            name=input("Enter video name to update: ")
            time=input("Enter video time to update: ")
            update_video(video_id,name,time)
        elif choice=='4':
            video_id=input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice=='5':
             break
        else:
            print("invalid input !")
    conn.close()

if __name__=="__main__":
    main()