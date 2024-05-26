from src import ImageProcessing, PleiadesNeo, Spot

processing = ImageProcessing(PleiadesNeo())
processing.execute_fusion("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_harmonization("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_ortho("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_co_registration("DEV/BRUTAS/PNEO_123321.zip")


processing.sensor = Spot()
processing.execute_fusion("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_harmonization("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_ortho("DEV/BRUTAS/PNEO_123321.zip")
processing.execute_co_registration("DEV/BRUTAS/PNEO_123321.zip")