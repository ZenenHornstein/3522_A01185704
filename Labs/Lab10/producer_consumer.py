from threading import Thread
import city_processor
class CityOverheadTimes:
    def __init__(self):
        self._data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        pass

    def get(self) -> city_processor.CityOverheadTime:
        pass

    def __len__(self) -> int:
        pass

class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimes):
        super().__init__()

    def run(self) -> None:
        pass




    pass





def main():
    pass


if __name__ == '__main__':
    main()
