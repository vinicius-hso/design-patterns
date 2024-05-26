from src import ImageProcessing, PleiadesNeo, Spot

processing = ImageProcessing(PleiadesNeo())

processing.execute("DEV/BRUTAS/PNEO_123321.zip")

processing.sensor = Spot()

processing.execute("DEV/BRUTAS/PNEO_123321.zip")