class File_manager:
    @classmethod
    def read_file(cls, file_name): # file_name : 읽어올 파일의 이름. (Refrigerator.txt)
        with open(file_name, 'rt') as file:
            data = file.readlines()
        return data

    # file_name : 쓸 파일의 이름. (Refrigerator.txt) / file_contents : 파일에 쓸 내용이 담긴 list
    @classmethod
    def write_file(cls, file_name, contents):
        with open(file_name, 'wt') as file:
            for item in contents:
                file.write(item+"\n")
        return

#
if __name__ == "__main__":
    contents = ["test_data"]
    File_manager.write_file("test_data.txt", contents)