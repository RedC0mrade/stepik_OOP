class Gun:

    def __init__(self, count: int = 0):
        self.count = count

    def shoot(self):
        print("paf" if self.count % 2 else "pif")
        self.count += 1

    def shots_count(self):
        return self.count

    def shots_reset(self):
        self.count = 0


gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
