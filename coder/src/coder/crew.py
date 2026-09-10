from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools.sandbox_tools import sandbox_tools


@CrewBase
class Coder():
    """Coder crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    @agent
    def coder(self) -> Agent:
        return Agent(
            config=self.agents_config['coder'],
            verbose=True,
            tools=sandbox_tools
        )


    @task
    def coding_task(self) -> Task:
        return Task(
            config=self.tasks_config['coding_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coder crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
