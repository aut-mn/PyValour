# The main logging utility for PyValour
# Based off of https://github.com/autumnfied/AsyncLogger
# Modified to not save files
import asyncio
from datetime import datetime

class AsyncLogCollector:
    def __init__(self):
        self.log_format = "%(timestamp)s [%(level)s] %(message)s"
        self.log_queue = asyncio.Queue()
        self.log_levels = {'INFO': '\033[32mINFO\033[0m','WARN': '\033[33mWARN\033[0m','ERROR': '\033[31mERROR\033[0m','FATAL': '\033[31;1mFATAL\033[0m'}
    async def log(self, level, message):
        timestamp = self.get_colored_timestamp()
        formatted_message = self.log_format % {'timestamp': timestamp, 'level': self.log_levels.get(level, level), 'message': message}
        print(formatted_message)
    async def info(self, message): await self.log('INFO', message)
    async def warn(self, message): await self.log('WARN', message)
    async def error(self, message): await self.log('ERROR', message)
    async def fatal(self, message): await self.log('FATAL', message)
    def get_colored_timestamp(self): return '\033[90m' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\033[0m'
    def get_timestamp(self): return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    async def start_log_collection(self):
        while True:
            log_entry = await self.log_queue.get()
            print(log_entry)