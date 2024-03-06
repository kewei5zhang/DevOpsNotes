from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(5, 9)  # will make the simulated users wait between 5 and 9 seconds

    # @task is the key. For every running user, Locust creates a greenlet (micro-thread), that will call those methods.
    # @task(5) indicates the weight is 5.
    @task
    def simulation_endpoint(self):
        self.client.get("/simulation")

    @task(5)
    def red_endpoint(self):
        self.client.get("/red")

    @task
    def green_endpoint(self):
        self.client.get("/green")

    def on_start(self):
        pass