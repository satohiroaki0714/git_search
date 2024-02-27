import os
import subprocess

count = 0
name = "./out"
def search_git_objects(directory):
    # ディレクトリ内のファイルとディレクトリを取得
    global name
    with open(name, "a") as output_file:
        cyclecount = 1000
        global count
        for filename in os.listdir(directory):
            count += 1
            # ファイルまたはディレクトリの絶対パス
            print(count)
            if count % cyclecount == 0:
                name += "1"
                print(name)
            path = os.path.join(directory, filename)

            # ディレクトリの場合は再帰的に探索
            if os.path.isdir(path):
                search_git_objects(path)

            # ファイルの場合は内容を表示
            else:
                sha1 = os.path.relpath(path, '.git/objects/')
                sha1 = sha1.replace(os.path.sep, '')  # スラッシュを削除
                print(sha1)
                try:
                    result = subprocess.run(["git", "cat-file", "-p", sha1], capture_output=True, text=True)
                    output_file.write(result.stdout)
                except:
                    print("error:")
                    print(sha1)



if __name__ == "__main__":
    git_objects_directory = ".git/objects"
    search_git_objects(git_objects_directory)
