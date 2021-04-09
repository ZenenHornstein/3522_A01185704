from concurrent.futures import ThreadPoolExecutor
from threading import Thread, Lock
import time
import city_processor

class CityOverheadTimeQueue:
    def __init__(self):
        self._data_queue = []
        self._access_queue_lock = Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Put a new item onto the back of the queue
        :param overhead_time: the item to add
        :return:
        """
        with self._access_queue_lock:
            self._data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        Get an item from the front of te queue and delete it.
        :return: the head of the que
        """
        with self._access_queue_lock:
            front = self._data_queue[0]
            del self._data_queue[0]
            return front

    def __len__(self) -> int:
        return len(self._data_queue)

class ProducerThread(Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self._city_list = cities
        self._queue = queue

    def run(self) -> None:
        for city in self._city_list:
            over_head_pass = city_processor.ISSDataRequest.get_overhead_pass(city)
            print(f"adding city number {len(self._queue)}:  {city.city_name} to Queue")
            self._queue.put(over_head_pass)
            if self._city_list.index(city) % 5 == 0 and self._city_list.index(city) > 0  == 0:
                print("produced sleeping for 1")
                time.sleep(1)
        print("end of run function")



class ConsumerThread(Thread):

    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self._queue = queue
        self._data_incoming = True


    def run(self) -> None:
        while self._data_incoming or len(self._queue) > 0:
            if len(self._queue) == 0:
                print("sleepping for 0.75 cuz q is empty")
                time.sleep(0.75)
            q_item = self._queue.get()
            print(q_item)
            print("sleeping for 0.5 seconds")
        pass




def main():
    import city_processor
    city_database = city_processor.CityDatabase("city_locations_test.xlsx")

    size = len(city_database.city_db)

    first_partition = city_database.city_db[:size // 3]
    second_partition = city_database.city_db[size // 3: 2 * (size // 3)]
    third_partition = city_database.city_db[2 * (size // 3)::]

    # print(first_partition, second_partition, third_partition)
    q = CityOverheadTimeQueue()

    producers = [ProducerThread(first_partition, q), ProducerThread(second_partition, q),
                 ProducerThread(third_partition, q)]
    consumer_thread = ConsumerThread(q)

    with ThreadPoolExecutor() as executor:
        for producer in producers:
            executor.submit(producer.run())
        consumer_thread._data_incoming = False
        executor.submit(consumer_thread.run)



if __name__ == '__main__':
    main()
