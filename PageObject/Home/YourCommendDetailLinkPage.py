from PageObject import Pages


class YourCommendDetailLinkPage:
    '''
    为您推荐浏览历史
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

    def operate(self):  # 操作步骤
        self.page.operate()

    def checkPoint(self):  # 检查点
        self.page.checkPoint()


if __name__ == "__main__":
    pass
