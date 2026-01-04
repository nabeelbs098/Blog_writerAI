from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dotenv import load_dotenv
import os

load_dotenv()

@CrewBase
class BlogCrew():
    """Blog Writing Crew"""
    agents_config = 'agents.yaml'
    tasks_config = 'tasks.yaml'

    # WE REMOVED THE LLM CLASS DEFINITION HERE TO PREVENT ERRORS

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            # PASS THE STRING DIRECTLY
            llm="groq/llama-3.3-70b-versatile"
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True,
            llm="groq/llama-3.3-70b-versatile"
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'],
            verbose=True,
            llm="groq/llama-3.3-70b-versatile"
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            agent=self.writer()
        )

    @task
    def editing_task(self) -> Task:
        return Task(
            config=self.tasks_config['editing_task'],
            agent=self.editor(),
            output_file='final_post.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher(), self.writer(), self.editor()],
            tasks=[self.research_task(), self.writing_task(), self.editing_task()],
            process=Process.sequential,
            verbose=True
        )