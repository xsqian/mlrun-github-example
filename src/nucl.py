import mlrun
def handler(context, event):
    project = mlrun.get_or_create_project(name="schedule-workflow", context="./")
    # project.set_source(source="git://github.com/xsqian/mlrun-github-example.git#main", pull_at_runtime=True)
    workflow_instance = project.run(
                    name="main",
                    watch=False,
                    engine="remote"
                    )
