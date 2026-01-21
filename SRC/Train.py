from Model_trainer import ModelTrainer
from Config import INTENT_PATH
from Utils import DatasetBuilder
from Intent_loader import IntentLoader


def main():
    loader = IntentLoader(INTENT_PATH)
    intents = loader.load_intents()
    dataset = DatasetBuilder(intents)
    x, y = dataset.build_dataset()
    trainer = ModelTrainer()
    trainer.train(x, y)

if __name__ == "__main__":
    main()