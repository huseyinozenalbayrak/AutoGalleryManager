class UI:
    def __init__(self,menu_items):
        self.menu_items = menu_items

    def show_menu(self):
        print("-" * 52, "|{:^50}|".format(" Menu "), "-"*52, sep="\n")
        for no,item in enumerate(self.menu_items):print("|{:^50}|".format(str(no+1)+"..."+item))
        print("-"*52)

    def get_choice(self):
        try:
            choice = int(input(f"Please select [1-{len(self.menu_items)}]: "))
            assert 1 <= choice <= len(self.menu_items), f"Please enter between [1-{len(self.menu_items)}]."
            return choice
        except AssertionError as e:
            print(e)
        except:
            print("Wrong Entry!")