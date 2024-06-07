
import time
import psutil


def nodegroup_test(context):
    context.logger.info("Resource Test!")
    mem = psutil.virtual_memory()
    vcpus = psutil.cpu_count(logical=True)
    pcpus = psutil.cpu_count(logical=False)
    context.logger.info(f"CPUs virtual  -> {vcpus}")
    context.logger.info(f"CPUs physical -> {pcpus}")
    context.logger.info(
        f"Memory avlbl  -> {round(mem.available/(1024 * 1024 * 1024), 2)}GB"
    )
    context.logger.info(f"Memory used   -> {round(mem.used/(1024 * 1024 * 1024), 2)}GB")
    context.logger.info(f"Sleeping 300s")
