import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="a",
                    format="We have next massage:%(asctimes):%(levelname)s:%(massages")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")














assert 2+2 == 5, "We have a error 1 line"











