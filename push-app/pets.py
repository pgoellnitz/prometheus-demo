from prometheus_client import Summary, Counter, CollectorRegistry, push_to_gateway
from random import randint, random
import time
import argparse

parser = argparse.ArgumentParser(description='Generate pet names.')
parser.add_argument('job_id',  type=int,
                    help='Job ID')
args = parser.parse_args()

registry = CollectorRegistry()
pet_exception_count = Counter('pet_exceptions',
                              'description of counter',
                              registry=registry)
pet_count = Counter(name='pet_counter_total',
                    documentation='a counter',
                    registry=registry,
                    labelnames=['name'])
pet_summary = Summary('pet_generation_latency', 'Description of summary',
                      registry=registry)

pets_available = ['cat', 'dog']


@pet_summary.time()
def pet():
    try:
        with pet_exception_count.count_exceptions():
                my_pet = pets_available[randint(0, 2)]
                pet_count.labels(my_pet).inc()
                time.sleep(random() / 2.0)
    except:
        pass


if __name__ == '__main__':
        num_pets = randint(1, 100)
        print("Generate {} pets.".format(num_pets))
        for i in range(num_pets):
            pet()
        print("Pushing for job id " + str(args.job_id))
        push_to_gateway('localhost:9091',
                        job='pet_job' + str(args.job_id),
                        registry=registry)
