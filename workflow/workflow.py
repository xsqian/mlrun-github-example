""" The main workflow of the project

This file creates the MLRun pipeline to run the functions
in an orchestrated manner

"""

from kfp import dsl
import mlrun


# Create a Kubeflow Pipelines pipeline
@dsl.pipeline(name="testing-resource")
def test():
    run2 = mlrun.run_function(
        name="nodegroup-test",
        function="nodegroup-test",
        local=False,
    )
