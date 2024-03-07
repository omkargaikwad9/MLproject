from src.MLproject import logger
from src.MLproject.exception import CustomException
import sys





if __name__ =="__main__":
    logger.logging.info("Excution has started")
    
    
    try:
        a = 1/0
    except Exception as e:
        logger.logging.info("custum exception working")
        raise CustomException(e,sys)