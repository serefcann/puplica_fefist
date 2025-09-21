import React from 'react'
import MarkdownRenderer from './MarkdownRenderer'

const MessageBubble = ({ message }) => {
  const { type, content, timestamp } = message

  const formatTime = (date) => {
    return date.toLocaleTimeString('tr-TR', { 
      hour: '2-digit', 
      minute: '2-digit' 
    })
  }

  const getBubbleClasses = () => {
    switch (type) {
      case 'user':
        return 'user-message message-bubble'
      case 'bot':
        return 'bot-message message-bubble'
      case 'error':
        return 'bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200 message-bubble mr-auto border border-red-200 dark:border-red-700'
      default:
        return 'bot-message message-bubble'
    }
  }

  const getContainerClasses = () => {
    switch (type) {
      case 'user':
        return 'flex justify-end'
      case 'bot':
      case 'error':
        return 'flex justify-start'
      default:
        return 'flex justify-start'
    }
  }

  return (
    <div className={getContainerClasses()}>
      <div className={`flex flex-col ${type === 'bot' ? 'max-w-4xl' : 'max-w-xs lg:max-w-md xl:max-w-lg'}`}>
        <div className={getBubbleClasses()}>
          {type === 'user' ? (
            <div className="whitespace-pre-wrap">{content}</div>
          ) : type === 'bot' ? (
            <div className="text-sm leading-relaxed">
              <MarkdownRenderer content={content} />
            </div>
          ) : (
            <MarkdownRenderer content={content} />
          )}
        </div>
        <div className={`text-xs text-gray-500 dark:text-gray-400 mt-1 px-2 ${
          type === 'user' ? 'text-right' : 'text-left'
        }`}>
          {formatTime(timestamp)}
        </div>
      </div>
    </div>
  )
}

export default MessageBubble


