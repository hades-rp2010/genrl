import gym

from genrl.environments import BaseWrapper


class GymWrapper(BaseWrapper, gym.Wrapper):
    """
    Wrapper class for all Gym Environments

    :param env: Gym environment name
    :param n_envs: Number of environments. None if not vectorised
    :param parallel: If vectorised, should environments be run through \
serially or parallelly
    :type env: string
    :type n_envs: None, int
    :type parallel: boolean
    """
    # TODO(zeus3101) Add functionality for VecEnvs
    def __init__(self, env):
        super(GymWrapper, self).__init__(env)
        self._env = env
        self.observation_space = self._env.observation_space
        self.action_space = self._env.action_space

    def __getattr__(self, name):
        """
        All other calls would go to base env
        """
        env = super(GymWrapper, self).__getattribute__('_env')
        return getattr(env, name)

    # TODO(zeus3101) Get get_state, set_state, get_info, get_done methods

    def render(self, mode="human"):
        """
        Renders all envs in a tiles format similar to baselines.

        :param mode: Can either be 'human' or 'rgb_array'. \
Displays tiled images in 'human' and returns tiled images in 'rgb_array'
        :type mode: string
        """
        self._env.render(mode=mode)

    def seed(self, seed=None):
        """
        Set environment seed

        :param seed: Value of seed
        :type seed: int
        """
        self._env.seed(seed)

    def step(self, action):
        """
        Steps the env through given action

        :param action: Action taken by agent
        :type action: NumPy array
        """
        return self._env.step(action)

    def reset(self):
        """
        Resets environment

        :returns: Initial state
        """
        return self._env.reset()

    def close(self):
        """
        Closes environment
        """
        self._env.close()
