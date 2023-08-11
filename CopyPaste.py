import os
import shutil


class CopyPaste:
    def __init__(self, des: str, scr: str) -> None:
        cwd = os.path.abspath(os.path.dirname(__file__))
        self.des = os.path.abspath(os.path.join(cwd, des))
        self.scr = os.path.abspath(os.path.join(cwd, scr))

    def copy_dir(self, dir_name: str) -> None:
        if os.path.exists(os.path.join(self.des, dir_name)) is False and\
                os.path.exists(os.path.join(self.scr, dir_name)) is True:
            print(os.path.join(self.des, dir_name))
            print(os.path.join(self.scr, dir_name))
            shutil.copytree(os.path.join(self.scr, dir_name), os.path.join(self.des, dir_name))

    def prepare_to_zip(self, dir_name: str) -> None:
        if os.path.exists(os.path.join(self.scr, dir_name)) is True:
            # print(os.path.join(self.scr, dir_name))
            contents_of_record = os.listdir(os.path.join(self.scr, dir_name))
            # print(contents_of_record)
            ready_to_remove: bool = False
            if "repairTicket_post.txt" in contents_of_record:
                file_path = os.path.join(self.scr, os.path.join(dir_name, "repairTicket_post.txt"))
                if os.path.exists(file_path) is True:
                    # print(file_path)
                    repair_ticket_post = open(file_path, 'r').read()
                    lines = repair_ticket_post.split('\n')
                    flag_board_pass: bool = False
                    for line in lines:
                        if str(line).find("# Board pass") != -1 and len(line) > 15:
                            flag_board_pass = True
                        if flag_board_pass is True and \
                                str(line).find("# Board fail") != -1 and len(line) == 15:
                            # print(len(line))
                            # print(line)
                            # print(file_path)
                            # print("ready to clean up")
                            ready_to_remove = True
                            flag_board_pass = False

                    if ready_to_remove is True:
                        # print(file_path)
                        # print("ready to clean up:")
                        for to_remove in contents_of_record:
                            if to_remove.find(".jpg") != -1:
                                if os.path.exists(os.path.join(self.scr, os.path.join(dir_name, to_remove))) is True:
                                    # pass
                                    # print(f".jpg to remove: {os.path.join(self.scr, os.path.join(dir_name, to_remove))}")
                                    os.remove(os.path.join(self.scr, os.path.join(dir_name, to_remove)))
                            if to_remove.find(".png") != -1:
                                if os.path.exists(os.path.join(self.scr, os.path.join(dir_name, to_remove))) is True:
                                    # pass
                                    # print(f".png to remove: {os.path.join(self.scr, os.path.join(dir_name, to_remove))}")
                                    os.remove(os.path.join(self.scr, os.path.join(dir_name, to_remove)))
                            if to_remove.find(".pgm") != -1:
                                if os.path.exists(os.path.join(self.scr, os.path.join(dir_name, to_remove))) is True:
                                    # pass
                                    # print(f".pgm to remove: {os.path.join(self.scr, os.path.join(dir_name, to_remove))}")
                                    os.remove(os.path.join(self.scr, os.path.join(dir_name, to_remove)))

                        ready_to_remove = False

    def zip_day(self, dir_name: str) -> None:
        if os.path.exists(os.path.join(self.des, dir_name)) is False and\
                os.path.exists(os.path.join(self.scr, dir_name)) is True:
            print(os.path.join(self.des, dir_name))
            print(os.path.join(self.scr, dir_name))
            shutil.make_archive(os.path.join(self.des, dir_name), 'zip',
                                os.path.join(self.scr, dir_name))
            # TODO remove directory from scr
            os.remove(os.path.join(self.scr, dir_name))
