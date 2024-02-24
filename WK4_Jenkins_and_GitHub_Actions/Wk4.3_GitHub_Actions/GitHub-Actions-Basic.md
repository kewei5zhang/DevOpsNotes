# GitHub Actions Basic

Quickstart doc: https://docs.github.com/en/actions/quickstart

You only need a GitHub repository to create and run a GitHub Actions workflow. In this guide, you'll add a workflow that demonstrates some of the essential features of GitHub Actions.

The following example shows you how GitHub Actions jobs can be automatically triggered, where they run, and how they can interact with the code in your repository.

## Creating your first workflow

1. Create a `.github/workflows` directory in your repository on GitHub if this directory does not already exist.

2. In the `.github/workflows` directory, create a file named `github-actions-demo.yml`. For more information, see "Creating new files."

3. Copy the following YAML contents into the `github-actions-demo.yml` file:

    ```yaml
    name: GitHub Actions Demo
    run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
    on: [push]
    jobs:
      Explore-GitHub-Actions:
        runs-on: ubuntu-latest
        steps:
          - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
          - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
          - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
          - name: Check out repository code
            uses: actions/checkout@v3
          - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
          - run: echo "🖥️ The workflow is now ready to test your code on the runner."
          - name: List files in the repository
            run: |
              ls ${{ github.workspace }}
          - run: echo "🍏 This job's status is ${{ job.status }}."
    ```

4. Scroll to the bottom of the page and select **Create a new branch for this commit and start a pull request**. Then, to create a pull request, click **Propose new file**.

    ![Alt Text](https://docs.github.com/assets/cb-67235/images/help/repository/actions-quickstart-commit-new-file.png)

    Committing the workflow file to a branch in your repository triggers the push event and runs your workflow.

## Understanding the workflow file

https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions#understanding-the-workflow-file

## Encrypted secrets

https://docs.github.com/en/actions/security-guides/encrypted-secrets

## Replace environment variables

https://github.com/danielr1996/envsubst-action

```yml
      - name: Replace Environment Variables
        uses: danielr1996/envsubst-action@1.0.0
        env:
          PORT: ${{ secrets.PORT }}
          DB_HOST: ${{ secrets.DB_HOST }}
          DB_USERNAME: ${{ secrets.DB_USERNAME }}
          DB_PORT: ${{ secrets.DB_PORT }}
          DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
          DB_NAME: ${{ secrets.DB_NAME }}
        with:
          input: deployment.yml
          output: deploy.yml
```

## Manually triggered workflows

https://docs.github.com/en/actions/using-workflows/triggering-a-workflow#defining-inputs-for-manually-triggered-workflows

```yml
on:
  workflow_dispatch:
```