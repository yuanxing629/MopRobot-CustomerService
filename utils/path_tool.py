"""
为整个工程提供统一的绝对路径
"""
import os


def get_project_root() -> str:
    """
        获取工程所在的根目录
        :return: 字符串根目录
        """
    # 当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # print(current_file)

    # 获取工程的根目录，先获取文件所在的文件夹绝对路径
    current_dir = os.path.dirname(current_file)
    # print(current_dir)

    # 获取工程根目录
    project_root = os.path.dirname(current_dir)
    # print(project_root)

    return project_root


def get_abs_path(relative_path: str) -> str:
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)


if __name__ == '__main__':
    # get_project_root()
    print(get_abs_path("config/config.txt"))
