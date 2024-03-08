from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)  # Our class defines a wait_time that will make the simulated users wait between 1 and 5 seconds after each task (see below) is executed.

    # @task is the key. For every running user, Locust creates a greenlet (micro-thread), that will call those methods.
    @task
    def simulation_endpoint(self):
        self.client.get("/simulation")

    @task(3) # The weight of this task is 2, which means it will be called twice as often as the other tasks.
    def red_endpoint(self):
        self.client.get("/red")

    @task
    def green_endpoint(self):
        self.client.get("/green")

    def on_start(self):
        pass