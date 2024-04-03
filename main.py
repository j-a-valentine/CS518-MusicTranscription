from segment import Segment
from gui import GUI


def main():
    seg = Segment("watermelon sugar high")
    seg.predict_ai("water melon sugar hi")
    seg.predict_human("watermelon sugar high")
    print(f"human score: {seg.score_human()} ai score: {seg.score_ai()}")

    gui = GUI("test title")



if __name__ == "__main__":
    main()