import apache_beam as beam
from apache_beam.testing.test_pipeline import TestPipeline
from apache_beam.testing.util import assert_that


def expected_nums():
   def _expected_nums(actual):
       assert actual[0] == 0
       assert actual[1] == 1

   return _expected_nums


def test_pipeline_without_assert_that():
   with TestPipeline() as p:
       _ = p | beam.Create([0, 1])


def test_assert_that():
   with TestPipeline() as p:
       nums = p | beam.Create([0, 1])
       assert_that(nums, expected_nums())

